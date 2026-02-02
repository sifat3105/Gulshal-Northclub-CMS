import json
from datetime import date, timedelta

from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.urls import reverse
from django.utils import timezone

from apps.about.models import BoardMember
from apps.contact.models import Appointment
from apps.events.models import Event
from apps.facilities.models import Place
from apps.gallery.models import Gallery
from apps.notice.models import NoticeCard


def _shift_month(base: date, delta: int) -> date:
    """Return first day of month shifted by delta months."""
    year = base.year + ((base.month - 1 + delta) // 12)
    month = ((base.month - 1 + delta) % 12) + 1
    return date(year, month, 1)


def _appointments_chart_data(month_count: int = 6) -> tuple[str, str]:
    month_start = timezone.localdate().replace(day=1)
    start = _shift_month(month_start, -(month_count - 1))

    month_labels = []
    month_map = {}
    for i in range(month_count):
        month = _shift_month(start, i)
        month_key = month.strftime("%Y-%m")
        month_labels.append(month.strftime("%b"))
        month_map[month_key] = 0

    monthly_counts = (
        Appointment.objects.filter(created_at__date__gte=start)
        .annotate(month=TruncMonth("created_at"))
        .values("month")
        .annotate(total=Count("id"))
        .order_by("month")
    )

    for row in monthly_counts:
        month_key = row["month"].strftime("%Y-%m")
        if month_key in month_map:
            month_map[month_key] = row["total"]

    values = [month_map[key] for key in month_map]

    chart = {
        "labels": month_labels,
        "datasets": [
            {
                "label": "Appointments",
                "data": values,
                "borderColor": "var(--color-primary-600)",
                "backgroundColor": "var(--color-primary-200)",
                "fill": True,
                "tension": 0.35,
                "pointRadius": 3,
            }
        ],
    }

    options = {
        "plugins": {"legend": {"display": False}},
        "scales": {
            "y": {"beginAtZero": True, "ticks": {"precision": 0}},
            "x": {"grid": {"display": False}},
        },
    }

    return json.dumps(chart), json.dumps(options)


def _events_chart_data() -> tuple[str, str]:
    event_type_labels = dict(Event.EVENT_TYPE_CHOICES)
    selected = ["running", "upcoming", "past", "completed"]

    counts = {key: 0 for key in selected}
    for row in Event.objects.values("event_type").annotate(total=Count("id")):
        key = row["event_type"]
        if key in counts:
            counts[key] = row["total"]

    labels = [event_type_labels.get(key, key.title()) for key in selected]
    values = [counts[key] for key in selected]

    chart = {
        "labels": labels,
        "datasets": [
            {
                "label": "Events",
                "data": values,
                "backgroundColor": [
                    "var(--color-primary-400)",
                    "var(--color-primary-500)",
                    "var(--color-primary-600)",
                    "var(--color-primary-700)",
                ],
                "borderColor": "var(--color-primary-800)",
                "borderWidth": 1,
                "borderRadius": 8,
            }
        ],
    }

    options = {
        "plugins": {"legend": {"display": False}},
        "scales": {
            "y": {"beginAtZero": True, "ticks": {"precision": 0}},
            "x": {"grid": {"display": False}},
        },
    }

    return json.dumps(chart), json.dumps(options)


def admin_dashboard_callback(request, context):
    """Inject dashboard widgets and charts into Unfold admin index."""
    seven_days_ago = timezone.now() - timedelta(days=7)

    appointments_chart, appointments_chart_options = _appointments_chart_data()
    events_chart, events_chart_options = _events_chart_data()

    context["dashboard_stats"] = [
        {
            "title": "Appointments",
            "value": Appointment.objects.count(),
            "note": "Total contact requests",
            "icon": "mail",
        },
        {
            "title": "New in 7 days",
            "value": Appointment.objects.filter(created_at__gte=seven_days_ago).count(),
            "note": "Recent appointment messages",
            "icon": "schedule",
        },
        {
            "title": "Active Events",
            "value": Event.objects.filter(is_active=True).count(),
            "note": "Currently visible events",
            "icon": "event",
        },
        {
            "title": "Facilities",
            "value": Place.objects.count(),
            "note": "Configured place sections",
            "icon": "fitness_center",
        },
        {
            "title": "Gallery Blocks",
            "value": Gallery.objects.count(),
            "note": "Membership/Reservation/Menu pages",
            "icon": "photo_library",
        },
        {
            "title": "Board Members",
            "value": BoardMember.objects.count(),
            "note": "People listed in About page",
            "icon": "groups",
        },
    ]

    context["dashboard_chart_appointments"] = appointments_chart
    context["dashboard_chart_appointments_options"] = appointments_chart_options
    context["dashboard_chart_events"] = events_chart
    context["dashboard_chart_events_options"] = events_chart_options

    context["dashboard_quick_links"] = [
        {
            "title": "Home Content",
            "link": reverse("admin:home_hero_changelist"),
            "icon": "home",
        },
        {
            "title": "About Content",
            "link": reverse("admin:about_abouthero_changelist"),
            "icon": "article",
        },
        {
            "title": "Accommodation",
            "link": reverse("admin:accommodation_accommodationhero_changelist"),
            "icon": "hotel",
        },
        {
            "title": "Gallery",
            "link": reverse("admin:gallery_membershipgallery_changelist"),
            "icon": "photo",
        },
        {
            "title": "Events",
            "link": reverse("admin:events_runningevent_changelist"),
            "icon": "event",
        },
        {
            "title": "Contact Inbox",
            "link": reverse("admin:contact_appointment_changelist"),
            "icon": "mark_email_read",
        },
        {
            "title": "Footer",
            "link": reverse("admin:footer_footerbrand_changelist"),
            "icon": "web",
        },
        {
            "title": "Notice Board",
            "link": reverse("admin:notice_noticecard_changelist"),
            "icon": "campaign",
        },
    ]

    context["dashboard_recent_appointments"] = (
        Appointment.objects.order_by("-created_at").only("full_name", "email", "created_at")[:6]
    )
    context["dashboard_recent_notices"] = NoticeCard.objects.order_by("-notice_date").only(
        "notice_name", "notice_subject", "notice_date"
    )[:5]

    return context
