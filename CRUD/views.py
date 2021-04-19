from django.shortcuts import render
from django.http import Http404
from CRUD.models import Crud


def index(request):

    users = Crud.objects.all()

    context = {
        'users': users,
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_user(request):
    if request.method == "POST":

        user = Crud(
            name=request.POST['name'],
            email=request.POST['email'],
        )

        user.save()

        context = {
            'name': user.name,
            'email': user.email,
        }

        return render(
            template_name='added_user.html',
            request=request,
            context=context,
        )

    return render(
        template_name='add_user_form.html',
        request=request,
    )


def get_user(request, user_id):
    try:
        specific_user = Crud.objects.get(id=user_id)
    except Crud.DoesNotExist:
        raise Http404("User does not exist")

    context = {
        'name': specific_user.name,
        'email': specific_user.email,
    }

    return render(
        template_name='got_user.html',
        request=request,
        context=context
    )


def edit_user(request, user_id):
    try:
        specific_user = Crud.objects.get(id=user_id)
    except Crud.DoesNotExist:
        raise Http404("User does not exist")

    context = {
        'name': specific_user.name,
        'email': specific_user.email,
    }

    if request.method == "POST":
        if request.POST['name'] != '':
            specific_user.name = request.POST['name']
            specific_user.save()

        if request.POST['email'] != '':
            specific_user.email = request.POST['email']
            specific_user.save()

        context = {
            'name': specific_user.name,
            'email': specific_user.email,
        }

        return render(
            template_name='updated_user.html',
            request=request,
            context=context,
        )

    return render(
        template_name='edit_user_form.html',
        request=request,
        context=context
    )


def delete_user(request, user_id):
    try:
        specific_user = Crud.objects.get(id=user_id)
    except Crud.DoesNotExist:
        raise Http404("User does not exist")

    context = {
        'name': specific_user.name,
        'email': specific_user.email,
    }

    specific_user.delete()

    return render(
        template_name='deleted_user.html',
        request=request,
        context=context
    )
