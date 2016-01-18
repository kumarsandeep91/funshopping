from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from .models import User_Details

def register(request, template_name="registration/register.html"):
	if request.method == 'GET':
		return render_to_response(template_name, locals(),
			context_instance=RequestContext(request))
	elif request.method == 'POST':
		f_name = request.POST['f_name']
		l_name = request.POST['l_name']
		phone = request.POST['phone']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		re_password = request.POST['confirmation']
		"""
			determining user type i.e buyer or seller and assigning them a integer value
		"""
		if request.POST['type'] == 'buyer':
			u_type = 0
		else:
			u_type = 1

		if password == re_password:
			# call create_user from ORM,
			user = auth.models.User.objects.create_user(username,email,password)
			user.first_name = f_name
			user.last_name = l_name
			user.save()
			"""adding users extra details"""
			u_details = User_Details(user=User.objects.get(id=user.id))
			u_details.u_type = u_type
			u_details.contact = phone
			u_details.save()
			return redirect('/accounts/login')
		else:
			warning = "Password does not matched"
			return render_to_response(template_name, locals(),
				context_instance=RequestContext(request))
def logout(request):
	auth.logout(request)
	return redirect('/accounts/login')

def login(request, template_name="registration/login.html"):
	if request.method == 'GET':
		return render_to_response(template_name, locals(),
			context_instance=RequestContext(request))
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				# for saving destination
				u_details = User_Details.objects.get(user=request.user.id)

				next = ""
				if next in request.GET:
					next = request.GET["next"]
				if next == None or next == "":
					next = "/catalog"
				return redirect(next)
				
			else:
				warning = "Your account is disabled"
				return render_to_response(template_name, locals(),
					context_instance=RequestContext(request))
		else:
			warning = "Invalid username or account"
			return render_to_response(template_name, locals(),
				context_instance=RequestContext(request))
	
@login_required
def my_account(request, template_name="registration/my_account.html"):
	page_title = 'My Account'
	# object of User_Details table for users extra information
	u_details = User_Details.objects.get(user=request.user.id)
	warning = ""
	if request.method == 'GET':
		getdata = request.GET.copy()
		if 'submit' in getdata:
			# display edit form
			if getdata['submit'] == 'edit':
				template_name="registration/edit_profile.html"
				return render_to_response(template_name, locals(),
					context_instance=RequestContext(request))
			elif getdata['submit'] == 'save':
				#update the details in database
				# pk = primary key
				u = User.objects.get(pk=request.user.id)
				if getdata['f_name']:
					u.first_name = getdata['f_name']
				if getdata['l_name']:
					u.last_name = getdata['l_name']
				if getdata['contact']:
					u_details.contact = getdata['contact']
				if getdata['sex']:
					u_details.sex = getdata['sex']
				if getdata['address']:
					u_details.address = getdata['address']
				u.save()
				u_details.save()
				warning = "Profile updated successfully"
				return render_to_response(template_name, locals(),
					context_instance=RequestContext(request))
			else:
				warning = ""
				template_name="registration/change_password.html"
				return render_to_response(template_name, locals(),
					context_instance=RequestContext(request))
		else:
			return render_to_response(template_name, locals(),
				context_instance=RequestContext(request))

	elif request.method == 'POST':
		postdata = request.POST.copy()
		if 'submit' in postdata:
			user = User.objects.get(id=request.user.id)
			if user is not None:
				if postdata['submit'] == "change":
					#check current password
					if user.check_password(postdata['curr_password']):
						#change password in database
						if postdata['new_password'] == postdata['re_password']:
							user.set_password(postdata['new_password'])
							user.save()
							warning = "Password changed successfully"
							#redirect to login page
							return redirect('/accounts/login')
						else:
							warning = "Password does not matched"
							template_name="registration/change_password.html"
					else:
						warning = "Invalid current password"
						template_name="registration/change_password.html"

			return render_to_response(template_name, locals(),
				context_instance=RequestContext(request))