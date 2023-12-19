import secrets

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .forms import ToolSelectionForm
from .models import ToolAttributeDefinition, ToolPickerResponses

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    
def tool_info(request):
    return render(request, "tool-detail.html")

def tool_selection_walkthrough(request):
    form = ToolSelectionForm()
    
    if request.method == 'POST':
        form = ToolSelectionForm(request.POST)

        if form.is_valid():
            intended_use_type = form.cleaned_data.get('intended_use_type')
            available_budget = form.cleaned_data.get('available_budget')
            setup_time = form.cleaned_data.get('setup_time')
            setup_complexity = form.cleaned_data.get('setup_complexity')
            
            # create a new instance of ToolPickerResponses
            new_response = ToolPickerResponses(
                unique_id=secrets.token_hex(8),
                intended_use_type=intended_use_type,
                available_budget=available_budget,
                setup_time=setup_time, 
                setup_complexity=setup_complexity
            )
            
            # store response unique_id to user's session
            request.session['submitted_form_id'] = new_response.unique_id
            
            # save new instance to db
            new_response.save()  
            request.session['tool_picker_page'] = form.cleaned_data 
            return redirect('tool_picker_results')

    return render(request, 'tool_picker_page.html', {'form': form})

def tool_picker_results(request):
    # load form id from user's session
    submitted_form_id = request.session.get('submitted_form_id')
    
    try:
        response = ToolPickerResponses.objects.get(unique_id=submitted_form_id)
        
        # bars multiplied by 25 for the percent-filled bars on the output page
        context = {
            'unique_id': response.unique_id,
            'intended_use_type': response.intended_use_type,
            'available_budget': response.available_budget,
            'available_budget_bar': int(response.available_budget) * 25,
            'setup_time': response.setup_time, 
            'setup_time_bar': int(response.setup_time) * 25,
            'setup_complexity': response.setup_complexity, 
            'setup_complexity_bar': int(response.setup_complexity) * 25,
        }
        
        return render(request, 'tool_picker_results.html', context=context)
    except ToolPickerResponses.DoesNotExist:
        return render(request, 'error_template.html', {'message': 'Response not found for this form ID'})

def get_cost_data(request):
    if request.method == 'GET' and 'selected_value_budget' in request.GET:
        selected_value_budget = request.GET.get('selected_value_budget')

        # logic to fetch data based on selected_value_budget from the database
        field_mapping = {
            '1': 'cost1',
            '2': 'cost2',
            '3': 'cost3',
            '4': 'cost4'
        }
    
        field_name = field_mapping.get(selected_value_budget)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                cost_value = tool_data.get(field_name)
                return JsonResponse({field_name: cost_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def get_setup_time_data(request):
    if request.method == 'GET' and 'selected_value_setup_time' in request.GET:
        selected_value_setup_time = request.GET.get('selected_value_setup_time')
    
        # logic to fetch data based on selected_value_setup_time from the database
        field_mapping = {
            '1': 'setup_time1',
            '2': 'setup_time2',
            '3': 'setup_time3',
            '4': 'setup_time4'
        }
    
        field_name = field_mapping.get(selected_value_setup_time)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                setup_time_value = tool_data.get(field_name)
                return JsonResponse({field_name: setup_time_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_setup_complexity_data(request):
    if request.method == 'GET' and 'selected_value_setup_complexity' in request.GET:
        selected_value_setup_complexity = request.GET.get('selected_value_setup_complexity')
    
        # logic to fetch data based on selected_value_setup_complexity from the database
        field_mapping = {
            '1': 'setup_complexity1',
            '2': 'setup_complexity2',
            '3': 'setup_complexity3',
            '4': 'setup_complexity4'
        }
    
        field_name = field_mapping.get(selected_value_setup_complexity)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                setup_complexity_value = tool_data.get(field_name)
                return JsonResponse({field_name: setup_complexity_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)