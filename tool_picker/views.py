import secrets

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .forms import ToolSelectionForm
from .models import ToolAttributeDefinition, ToolPickerResponses, Tool

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    
def tool_info(request, tool_id):
    tool = Tool.objects.get(id=tool_id)
    
    context = {
        'tool_name': tool.name,
        'tool_description': tool.description,
    }
    
    return render(request, "tool-detail.html", context=context)

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
            return redirect('tool_picker_results', new_response.unique_id)
        # if the form is not valid, re-render the form with user input
        else:
            return render(request, 'tool_picker_page.html', {'form': form})
    else:
        # GET request or when form is not submitted
        form = ToolSelectionForm(initial=request.session.get('tool_picker_page', None))
    
    return render(request, 'tool_picker_page.html', {'form': form})

def edit_form_submission(request, unique_id):
    submission = get_object_or_404(ToolPickerResponses, unique_id=unique_id)  
    
    if request.method == 'POST':
        form = ToolSelectionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = ToolSelectionForm(instance=submission)
    
    return render(request, 'edit_form_template.html', {'form': form})

def tool_picker_results(request, response_id):
    top_recommendation = find_best_match(request, response_id)
    top_recommendation_information = Tool.objects.get(name=top_recommendation.name)
    
    # send user to error page if no form found in their session
    if not response_id: 
        return render(request, 'error_no_submitted_form.html')
    
    try:
        response = ToolPickerResponses.objects.get(unique_id=response_id)
        
        # bars multiplied by 25 for the percent-filled bars on the output page
        context = {
            'unique_id': response.unique_id,
            'top_recommendation_name': top_recommendation_information.name,
            'top_recommendation_description': top_recommendation_information.description,
            'top_recommendation_setup_speed': top_recommendation_information.setup_speed,
            'top_recommendation_setup_speed_desc': top_recommendation_information.setup_speed_desc,
            'top_recommendation_setup_complexity': top_recommendation_information.setup_complexity,
            'top_recommendation_setup_complexity_desc': top_recommendation_information.setup_complexity_desc,
            'top_recommendation_maintenance_complexity': top_recommendation_information.maintenance_complexity,
            'top_recommendation_maintenance_complexity_desc': top_recommendation_information.maintenance_complexity_desc,
            'top_recommendation_training_and_support': top_recommendation_information.training_and_support,
            'top_recommendation_training_and_support_desc': top_recommendation_information.training_and_support_desc,
            'top_recommendation_transition': top_recommendation_information.transition,
            'top_recommendation_transition_desc': top_recommendation_information.transition_desc,
            'top_recommendation_performance': top_recommendation_information.performance,
            'top_recommendation_performance_desc': top_recommendation_information.performance_desc,
            'top_recommendation_connectivity': top_recommendation_information.connectivity,
            'top_recommendation_connectivity_desc': top_recommendation_information.connectivity_desc,
            'top_recommendation_data_cleaning': top_recommendation_information.data_cleaning,
            'top_recommendation_data_cleaning_desc': top_recommendation_information.data_cleaning_desc,
            'top_recommendation_data_viz': top_recommendation_information.data_viz,
            'top_recommendation_data_viz_desc': top_recommendation_information.data_viz_desc,
            'top_recommendation_data_management_policies': top_recommendation_information.data_management_policies,
            'top_recommendation_data_management_policies_desc': top_recommendation_information.data_management_policies_desc,
            'top_recommendation_interoperability': top_recommendation_information.interoperability,
            'top_recommendation_interoperability_desc': top_recommendation_information.interoperability_desc,
            'top_recommendation_localization': top_recommendation_information.localization,
            'top_recommendation_localization_desc': top_recommendation_information.localization_desc,
            'top_recommendation_data_privacy': top_recommendation_information.data_privacy,
            'top_recommendation_data_privacy_desc': top_recommendation_information.data_privacy_desc,
            'top_recommendation_data_protection': top_recommendation_information.data_protection,
            'top_recommendation_data_protection_desc': top_recommendation_information.data_protection_desc,
            'top_recommendation_cost': top_recommendation_information.cost,
            'top_recommendation_cost_desc': top_recommendation_information.cost_desc,
            
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
            'top_recommendation': top_recommendation,
        }
        
        return render(request, 'tool_picker_results.html', context=context)
    except ToolPickerResponses.DoesNotExist:
        return render(request, 'error_template.html', {'message': 'Response not found for this form ID'})

def find_best_match(request, response_id):
    try:
        # retrieve user response
        user_response = ToolPickerResponses.objects.get(unique_id=response_id)
    except ToolPickerResponses.DoesNotExist:
        return render(request, 'error_no_submitted_form.html', {'message': 'Response not found'})
    
    # load all tools
    toolbox = Tool.objects.all()
    
    best_match = None
    winning_score = -1000 # arbitrarily low number as placeholder
    
    # score each tool based on how well it matches the user's needs
    for tool in toolbox:
        budget_diff = tool.cost - user_response.available_budget
        print(f'{tool.name} budget difference: {budget_diff}')
        
        budget_score = score_response(budget_diff)
        print(f'{tool.name} budget score: {budget_score}')
        
        setup_time_diff = tool.setup_speed - user_response.setup_time
        print(f'{tool.name} setup speed difference: {setup_time_diff}')
        
        setup_time_score = score_response(setup_time_diff)
        print(f'{tool.name} setup speed score: {setup_time_score}')
        
        setup_complexity_diff = tool.setup_speed - user_response.setup_complexity
        print(f'{tool.name} setup complexity difference: {setup_complexity_diff}')
        
        setup_complexity_score = score_response(setup_complexity_diff)
        print(f'{tool.name} setup complexity score: {setup_complexity_score}')
        
        maintenance_diff = tool.maintenance_complexity - user_response.maintenance
        print(f'{tool.name} maintenance difference: {maintenance_diff}')
        
        maintenance_score = score_response(maintenance_diff)
        print(f'{tool.name} maintenance score: {maintenance_score}')
        
        closeout_diff = tool.transition - user_response.closeout
        print(f'{tool.name} closeout difference: {closeout_diff}')
        
        closeout_score = score_response(closeout_diff)
        print(f'{tool.name} closeout score: {closeout_score}')

    
        # sum the differences to get a total "difference score"
        total_tool_score = budget_score + setup_time_score + setup_complexity_score + maintenance_score
        print(f'{tool.name} TOTAL DIFFERENCE: {total_tool_score}')
        
        
        # if this tool is a better match than the previous best, remember it
        if total_tool_score > winning_score:
            best_match = tool
            winning_score = total_tool_score
    
    # check if a match was found
    if best_match is None:
        return render(request, 'error.html', {'message': 'No suitable tool found'})
    
    # return the name of the best matching tool
    return best_match

def score_response(input_variable):
    """
    Takes in a variable from the selection framework, and scores it based on the difference against the tool.
    The weighting exaggerates differences between the user's choice and the compared tool's attributes.
    
    Parameters:
    input_variable (int): An integer between 3 and -3
    
    Returns:
    int:Returning value as output_score
    """
    
    if input_variable == 3:
        output_score = -5
    elif input_variable == 2:
        output_score = -3
    elif input_variable == 1:
        output_score = -1
    elif input_variable == 0:
        output_score = 1
    else:
        output_score = 3
    
    return output_score

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