import secrets

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .forms import ToolSelectionForm
from .models import ToolAttributeDefinition, ToolPickerResponses, Tool

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    
def tool_info(request):
    return render(request, "tool-detail.html")

def tool_selection_walkthrough(request):
    if request.method == 'POST':
        form = ToolSelectionForm(request.POST)
        if form.is_valid():
            # extract cleaned data
            cleaned_data = form.cleaned_data
    
            # create a new instance of ToolPickerResponses
            new_response = ToolPickerResponses(
                unique_id=secrets.token_hex(8),
                intended_use_type=cleaned_data['intended_use_type'],
                available_budget=cleaned_data['available_budget'],
                setup_time=cleaned_data['setup_time'],
                setup_complexity=cleaned_data['setup_complexity'],
                maintenance=cleaned_data['maintenance'],
                closeout=cleaned_data['closeout'],
                support=cleaned_data['support'],
                performance=cleaned_data['performance'],
                connectivity=cleaned_data['connectivity'],
                data_cleaning=cleaned_data['data_cleaning'],
                data_viz=cleaned_data['data_viz'],
                interoperability=cleaned_data['interoperability'],
                localization=cleaned_data['localization'],
                data_privacy=cleaned_data['data_privacy'],
                data_protection=cleaned_data['data_protection']
            )
    
            # store response unique_id to user's session
            request.session['submitted_form_id'] = new_response.unique_id
    
            # save new instance to the database
            new_response.save()
            request.session['tool_picker_page'] = cleaned_data
            return redirect('tool_picker_results')
        # if the form is not valid, re-render the form with user input
        else:
            return render(request, 'tool_picker_page.html', {'form': form})
    else:
        # for GET request or when form is not submitted
        form = ToolSelectionForm(initial=request.session.get('tool_picker_page', None))
    
    return render(request, 'tool_picker_page.html', {'form': form})

def edit_form_submission(request, unique_id):
    submission = get_object_or_404(ToolPickerResponses, unique_id=unique_id)  
    
    if request.method == 'POST':
        form = ToolSelectionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page.
    else:
        form = ToolSelectionForm(instance=submission)
    
    return render(request, 'edit_form_template.html', {'form': form})

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
            'maintenance': response.maintenance, 
            'maintenance_bar': int(response.maintenance) * 25,
            'closeout': response.closeout, 
            'closeout_bar': int(response.closeout) * 25,
            'support': response.support, 
            'support_bar': int(response.support) * 25,
            'performance': response.performance, 
            'performance_bar': int(response.performance) * 25,
            'connectivity': response.connectivity, 
            'connectivity_bar': int(response.connectivity) * 25,
            'data_cleaning': response.data_cleaning, 
            'data_cleaning_bar': int(response.data_cleaning) * 25,
            'data_viz': response.data_viz, 
            'data_viz_bar': int(response.data_viz) * 25,
            'interoperability': response.interoperability, 
            'interoperability_bar': int(response.interoperability) * 25,
            'localization': response.localization, 
            'localization_bar': int(response.localization) * 25,
            'data_privacy': response.data_privacy, 
            'data_privacy_bar': int(response.data_privacy) * 25,
            'data_protection': response.data_protection, 
            'data_protection_bar': int(response.data_protection) * 25,
        }
        
        
        
        return render(request, 'tool_picker_results.html', context=context)
    except ToolPickerResponses.DoesNotExist:
        return render(request, 'error_template.html', {'message': 'Response not found for this form ID'})

def load_toolbox(request):
    context = {
        'tools_data': Tool.objects.all()
    }
    
    for tool in context['tools_data']:
        print(tool)
    
    return render(request, 'tool_picker_results.html', context=context)

def find_best_match(request):
    
    pass

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

    # return JsonResponse({'error': 'Invalid request'}, status=400)
    
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

def get_maintenance_data(request):
    if request.method == 'GET' and 'selected_value_maintenance' in request.GET:
        selected_value_maintenance = request.GET.get('selected_value_maintenance')
    
        # logic to fetch data based on selected_value_maintenance from the database
        field_mapping = {
            '1': 'maintenance1',
            '2': 'maintenance2',
            '3': 'maintenance3',
            '4': 'maintenance4'
        }
    
        field_name = field_mapping.get(selected_value_maintenance)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                maintenance_value = tool_data.get(field_name)
                return JsonResponse({field_name: maintenance_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_closeout_data(request):
    if request.method == 'GET' and 'selected_value_closeout' in request.GET:
        selected_value_closeout = request.GET.get('selected_value_closeout')
    
        # logic to fetch data based on selected_value_closeout from the database
        field_mapping = {
            '1': 'closeout1',
            '2': 'closeout2',
            '3': 'closeout3',
            '4': 'closeout4'
        }
    
        field_name = field_mapping.get(selected_value_closeout)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                closeout_value = tool_data.get(field_name)
                return JsonResponse({field_name: closeout_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def get_support_data(request):
    if request.method == 'GET' and 'selected_value_support' in request.GET:
        selected_value_support = request.GET.get('selected_value_support')
    
        # logic to fetch data based on selected_value_support from the database
        field_mapping = {
            '1': 'support1',
            '2': 'support2',
            '3': 'support3',
            '4': 'support4'
        }
    
        field_name = field_mapping.get(selected_value_support)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                support_value = tool_data.get(field_name)
                return JsonResponse({field_name: support_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_performance_data(request):
    if request.method == 'GET' and 'selected_value_performance' in request.GET:
        selected_value_performance = request.GET.get('selected_value_performance')
    
        # logic to fetch data based on selected_value_performance from the database
        field_mapping = {
            '1': 'performance1',
            '2': 'performance2',
            '3': 'performance3',
            '4': 'performance4'
        }
    
        field_name = field_mapping.get(selected_value_performance)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                performance_value = tool_data.get(field_name)
                return JsonResponse({field_name: performance_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_connectivity_data(request):
    if request.method == 'GET' and 'selected_value_connectivity' in request.GET:
        selected_value_connectivity = request.GET.get('selected_value_connectivity')
    
        # logic to fetch data based on selected_value_connectivity from the database
        field_mapping = {
            '1': 'connectivity1',
            '2': 'connectivity2',
            '3': 'connectivity3',
            '4': 'connectivity4'
        }
    
        field_name = field_mapping.get(selected_value_connectivity)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                connectivity_value = tool_data.get(field_name)
                return JsonResponse({field_name: connectivity_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def get_data_cleaning_data(request):
    if request.method == 'GET' and 'selected_value_data_cleaning' in request.GET:
        selected_value_data_cleaning = request.GET.get('selected_value_data_cleaning')
    
        # logic to fetch data based on selected_value_data_cleaning from the database
        field_mapping = {
            '1': 'data_cleaning1',
            '2': 'data_cleaning2',
            '3': 'data_cleaning3',
            '4': 'data_cleaning4'
        }
    
        field_name = field_mapping.get(selected_value_data_cleaning)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                data_cleaning_value = tool_data.get(field_name)
                return JsonResponse({field_name: data_cleaning_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_data_viz_data(request):
    if request.method == 'GET' and 'selected_value_data_viz' in request.GET:
        selected_value_data_viz = request.GET.get('selected_value_data_viz')
    
        # logic to fetch data based on selected_value_data_viz from the database
        field_mapping = {
            '1': 'data_viz1',
            '2': 'data_viz2',
            '3': 'data_viz3',
            '4': 'data_viz4'
        }
    
        field_name = field_mapping.get(selected_value_data_viz)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                data_viz_value = tool_data.get(field_name)
                return JsonResponse({field_name: data_viz_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def get_interoperability_data(request):
    if request.method == 'GET' and 'selected_value_interoperability' in request.GET:
        selected_value_interoperability = request.GET.get('selected_value_interoperability')
    
        # logic to fetch data based on selected_value_interoperability from the database
        field_mapping = {
            '1': 'interoperability1',
            '2': 'interoperability2',
            '3': 'interoperability3',
            '4': 'interoperability4'
        }
    
        field_name = field_mapping.get(selected_value_interoperability)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                interoperability_value = tool_data.get(field_name)
                return JsonResponse({field_name: interoperability_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def get_localization_data(request):
    if request.method == 'GET' and 'selected_value_localization' in request.GET:
        selected_value_localization = request.GET.get('selected_value_localization')
    
        # logic to fetch data based on selected_value_localization from the database
        field_mapping = {
            '1': 'localization1',
            '2': 'localization2',
            '3': 'localization3',
            '4': 'localization4'
        }
    
        field_name = field_mapping.get(selected_value_localization)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                localization_value = tool_data.get(field_name)
                return JsonResponse({field_name: localization_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def get_data_privacy_data(request):
    if request.method == 'GET' and 'selected_value_data_privacy' in request.GET:
        selected_value_data_privacy = request.GET.get('selected_value_data_privacy')
    
        # logic to fetch data based on selected_value_data_privacy from the database
        field_mapping = {
            '1': 'data_privacy1',
            '2': 'data_privacy2',
            '3': 'data_privacy3',
            '4': 'data_privacy4'
        }
    
        field_name = field_mapping.get(selected_value_data_privacy)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                data_privacy_value = tool_data.get(field_name)
                return JsonResponse({field_name: data_privacy_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def get_data_protection_data(request):
    if request.method == 'GET' and 'selected_value_data_protection' in request.GET:
        selected_value_data_protection = request.GET.get('selected_value_data_protection')
    
        # logic to fetch data based on selected_value_data_protection from the database
        field_mapping = {
            '1': 'data_protection1',
            '2': 'data_protection2',
            '3': 'data_protection3',
            '4': 'data_protection4'
        }
    
        field_name = field_mapping.get(selected_value_data_protection)
        if not field_name:
            return JsonResponse({'error': 'Invalid selected value'}, status=400)
    
        try:
            # fetch data from the database based on the selected field name
            tool_data = ToolAttributeDefinition.objects.values(field_name).first()
            if tool_data:
                data_protection_value = tool_data.get(field_name)
                return JsonResponse({field_name: data_protection_value})
            else:
                return JsonResponse({'error': f'No data found for {field_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)