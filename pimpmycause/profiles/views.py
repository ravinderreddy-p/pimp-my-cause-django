from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory

from registration.backends.default import views as registration_views
from profiles.forms import (
    PimpUserRegistrationForm,
    PimpUserProfileForm,
    MarketerUserProfileForm,
    CauseUserProfileForm,
    QualificationForm
)
from profiles.models import PimpUser, Qualification
from adverts.models import Advert
import logging

log = logging.getLogger("pimpmycause")


class RegistrationView(registration_views.RegistrationView):
    """The Registration view."""
    template_name = 'registration/registration_form.html'
    form_class = PimpUserRegistrationForm
    success_url = '/accounts/registration/complete/'


class ActivationComplete(TemplateView):
    """The Activation Complete view."""

    template_name = 'registration/activate_complete.html'


def profile_detail(request, user_id):
    user = get_object_or_404(
        PimpUser,
        id=user_id,
    )

    if user.usertype == PimpUser.CAUSE:
        adverts_list = (
            Advert.objects
            .all()
            .filter(cause_profile=user_id)
        )

        context = {
            'adverts_list': adverts_list,
            'profile_user': user
        }

    else:
        context = {'profile_user': user}

    return render(request, 'profiles/detail.html', context)


@login_required
def profile_edit(request):
    """Edit user profile."""

    if (request.user.usertype == PimpUser.ADMIN):
        return redirect('homepage')
    print("HERE")
    QualificationFormSet = modelformset_factory(
        Qualification,
        QualificationForm,
        extra=3,
        min_num=2,
        validate_min=True,
        fields=('name', 'description', 'start_date', 'end_date')
    )

    print("before Post")

    if request.method == 'POST':
        profile_update_form = PimpUserProfileForm(
            request.POST,
            instance=request.user
        )

        # MARKETER
        if (request.user.usertype == PimpUser.MARKETER):
            additional_profile_form = MarketerUserProfileForm(
                request.POST,
                instance=request.user.marketerprofile,
            )
            qualification_form_set = QualificationFormSet(
                request.POST,
                instance=request.user.marketerprofile,
            )
        # CAUSE
        elif (request.user.usertype == PimpUser.CAUSE):
            additional_profile_form = CauseUserProfileForm(
                request.POST,
            )
        # pdb.set_trace()

        if profile_update_form.is_valid() and additional_profile_form.is_valid():
            user_details = profile_update_form.save(commit=False)
            user_details.user = request.user
            user_details.save()

            profile_details = additional_profile_form.save(commit=False)
            profile_details.save()
            additional_profile_form.save_m2m()

            if request.user.usertype == PimpUser.MARKETER and qualification_form_set.is_valid():
                qualification_details = qualification_form_set.save(commit=False)
                for qualification in qualification_form_set:
                    qualification.marketer = request.user

                qualification_details.save_m2m()

            return redirect(
                'profile_detail',
                user_id=request.user.id
            )

    else:
        profile_update_form = PimpUserProfileForm(instance=request.user)

        # MARKETER
        if (request.user.usertype == PimpUser.MARKETER):
            additional_profile_form = MarketerUserProfileForm(
                instance=request.user.marketerprofile,
            )
            qualification_form = QualificationFormSet()
            print("qualification_form")

        # CAUSE
        else:
            additional_profile_form = CauseUserProfileForm(
                instance=request.user.causeprofile,
            )

    context = {
        'profile_update_form': profile_update_form,
        'additional_profile_form': additional_profile_form,
        'qualification_form': qualification_form
    }

    return render(request, 'profiles/profile.html', context)
