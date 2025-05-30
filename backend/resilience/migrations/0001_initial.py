# Generated by Django 5.1.8 on 2025-05-07 19:15

import django.db.models.deletion
import iam.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0070_auto_fix_finding_folider"),
        ("iam", "0011_replace_slash_in_folder_names"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BusinessImpactAnalysis",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="published"),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                ("eta", models.DateField(blank=True, null=True, verbose_name="ETA")),
                (
                    "due_date",
                    models.DateField(blank=True, null=True, verbose_name="Due date"),
                ),
                (
                    "version",
                    models.CharField(
                        blank=True,
                        default="1.0",
                        help_text="Version of the compliance assessment (eg. 1.0, 2.0, etc.)",
                        max_length=100,
                        null=True,
                        verbose_name="Version",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("planned", "Planned"),
                            ("in_progress", "In progress"),
                            ("in_review", "In review"),
                            ("done", "Done"),
                            ("deprecated", "Deprecated"),
                        ],
                        default="planned",
                        max_length=100,
                        null=True,
                        verbose_name="Status",
                    ),
                ),
                (
                    "observation",
                    models.TextField(blank=True, null=True, verbose_name="Observation"),
                ),
                (
                    "authors",
                    models.ManyToManyField(
                        blank=True,
                        related_name="%(class)s_authors",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Authors",
                    ),
                ),
                (
                    "folder",
                    models.ForeignKey(
                        default=iam.models.Folder.get_root_folder_id,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_folder",
                        to="iam.folder",
                    ),
                ),
                (
                    "perimeter",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.perimeter",
                        verbose_name="Perimeter",
                    ),
                ),
                (
                    "reviewers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="%(class)s_reviewers",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Reviewers",
                    ),
                ),
                (
                    "risk_matrix",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.riskmatrix",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AssetAssessment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="published"),
                ),
                ("recovery_documented", models.BooleanField(default=False)),
                ("recovery_tested", models.BooleanField(default=False)),
                ("recovery_targets_met", models.BooleanField(default=False)),
                ("observation", models.TextField(blank=True, null=True)),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.asset"
                    ),
                ),
                (
                    "associated_controls",
                    models.ManyToManyField(blank=True, to="core.appliedcontrol"),
                ),
                (
                    "dependencies",
                    models.ManyToManyField(
                        blank=True, related_name="dependencies", to="core.asset"
                    ),
                ),
                ("evidences", models.ManyToManyField(blank=True, to="core.evidence")),
                (
                    "folder",
                    models.ForeignKey(
                        default=iam.models.Folder.get_root_folder_id,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_folder",
                        to="iam.folder",
                    ),
                ),
                (
                    "bia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resilience.businessimpactanalysis",
                    ),
                ),
            ],
            options={
                "unique_together": {("bia", "asset")},
            },
        ),
        migrations.CreateModel(
            name="EscalationThreshold",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="published"),
                ),
                ("point_in_time", models.IntegerField()),
                ("quali_impact", models.IntegerField(default=-1)),
                ("quanti_impact", models.FloatField(default=0)),
                (
                    "quanti_impact_unit",
                    models.CharField(
                        choices=[
                            ("people", "People"),
                            ("currency", "Currency"),
                            ("records", "Records"),
                            ("man_hours", "Man-hours"),
                            ("data_gb", "Data (GB)"),
                            ("gu", "Generic Unit"),
                        ],
                        default="currency",
                        max_length=20,
                    ),
                ),
                ("justification", models.TextField(blank=True, null=True)),
                (
                    "asset_assessment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resilience.assetassessment",
                    ),
                ),
                (
                    "folder",
                    models.ForeignKey(
                        default=iam.models.Folder.get_root_folder_id,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_folder",
                        to="iam.folder",
                    ),
                ),
                (
                    "qualifications",
                    models.ManyToManyField(blank=True, to="core.qualification"),
                ),
            ],
            options={
                "unique_together": {("asset_assessment", "point_in_time")},
            },
        ),
    ]
