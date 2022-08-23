# Generated by Django 3.2.15 on 2022-08-23 16:59

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtail_editable_help.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('base', '0008_use_json_field_for_body_streamfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerypage',
            name='collection',
            field=models.ForeignKey(blank=True, help_text=wagtail_editable_help.models.HelpText('Gallery page collection', default='Select the image collection for this gallery.'), limit_choices_to=models.Q(('name__in', ['Root']), _negated=True), null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.collection'),
        ),
        migrations.AlterField(
            model_name='gallerypage',
            name='image',
            field=models.ForeignKey(blank=True, help_text=wagtail_editable_help.models.HelpText('Hero image', default='Landscape mode only; horizontal width between 1000px and 3000px.'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='gallerypage',
            name='introduction',
            field=models.TextField(blank=True, help_text=wagtail_editable_help.models.HelpText('Gallery page introduction', default='Text to describe the page')),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_section_1',
            field=models.ForeignKey(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page featured section 1', default='First featured section for the homepage. Will display up to three child items.'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Featured section 1'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_section_1_title',
            field=models.CharField(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page featured section title 1', default='Title to display above the promo copy'), max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_section_2',
            field=models.ForeignKey(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page featured section 2', default='Second featured section for the homepage. Will display up to three child items.'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Featured section 2'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_section_2_title',
            field=models.CharField(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page featured section title 2', default='Title to display above the promo copy'), max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_section_3',
            field=models.ForeignKey(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page featured section 3', default='Third featured section for the homepage. Will display up to six child items.'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Featured section 3'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_section_3_title',
            field=models.CharField(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page featured section title 3', default='Title to display above the promo copy'), max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_cta',
            field=models.CharField(help_text=wagtail_editable_help.models.HelpText('Home page hero CTA', default='Text to display on Call to Action'), max_length=255, verbose_name='Hero CTA'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_cta_link',
            field=models.ForeignKey(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page CTA link', default='Choose a page to link to for the Call to Action'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Hero CTA link'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_text',
            field=models.CharField(help_text=wagtail_editable_help.models.HelpText('Home page hero text', default='Write an introduction for the bakery'), max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text=wagtail_editable_help.models.HelpText('Hero image', default='Landscape mode only; horizontal width between 1000px and 3000px.'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='promo_image',
            field=models.ForeignKey(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page promo image', default='Promo image'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='promo_text',
            field=wagtail.fields.RichTextField(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page promo text', default='Write some promotional copy'), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='promo_title',
            field=models.CharField(blank=True, help_text=wagtail_editable_help.models.HelpText('Home page promo title', default='Title to display above the promo copy'), max_length=255),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text=wagtail_editable_help.models.HelpText('Hero image', default='Landscape mode only; horizontal width between 1000px and 3000px.'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='introduction',
            field=models.TextField(blank=True, help_text=wagtail_editable_help.models.HelpText('Standard page introduction', default='Text to describe the page')),
        ),
    ]
