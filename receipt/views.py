from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from .models import *



def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdf_view(request):
    context = {
        'title': 'PDF Title',
        'data': [
            {'column1': 'Row 1, Cell 1', 'column2': 'Row 1, Cell 2'},
            {'column1': 'Row 2, Cell 1', 'column2': 'Row 2, Cell 2'},
            {'column1': 'Row 3, Cell 1', 'column2': 'Row 3, Cell 2'},
        ],
    }
    return render_to_pdf('index.html', context)

def index(request):
    context = {
        'title': 'PDF Title',
        'data': [
            {'column1': 'Row 1, Cell 1', 'column2': 'Row 1, Cell 2'},
            {'column1': 'Row 2, Cell 1', 'column2': 'Row 2, Cell 2'},
            {'column1': 'Row 3, Cell 1', 'column2': 'Row 3, Cell 2'},
            {'column1': 'Row 3, Cell 1', 'column2': 'Row 3, Cell 2'},
            {'column1': 'Row 3, Cell 1', 'column2': 'Row 3, Cell 2'},
            {'column1': 'Row 3, Cell 1', 'column2': 'Row 3, Cell 2'},
            {'column1': 'Row 3, Cell 1', 'column2': 'Row 3, Cell 2'},
        ],
        'date': date.today()
    }
    return render(request,'form.html',context)



def transaction_view(request):
    if request.method == 'POST':
        # Retrieve and clean data from the POST request
        acc_details = request.POST.get('acc_details', '').strip()
        cust_reference = request.POST.get('cust_reference', '').strip()
        trans_date = request.POST.get('trans_date', '').strip()
        val_date = request.POST.get('val_date', '').strip()
        amount = request.POST.get('amount', '').strip()
        cheque_number = request.POST.get('cheque_number', '').strip()
        trans_ref = request.POST.get('trans_ref', '').strip()
        description = request.POST.get('description', '').strip()

        # Perform basic validation
        errors = []
        if not acc_details:
            errors.append("Account Details cannot be empty.")
        if not cust_reference:
            errors.append("Customer Reference cannot be empty.")
        if not trans_date:
            errors.append("Transaction Date is required.")
        if not val_date:
            errors.append("Value Date is required.")
        if not amount or float(amount) <= 0:
            errors.append("Amount must be a positive number.")
        if not trans_ref:
            errors.append("Transaction Reference Number cannot be empty.")

        if errors:
            return render(request, 'index.html', context = {'errors': errors,"data":data})
        
        # Save the data to the model if no errors
        transaction = TransactionForm(
            acc_details=acc_details,
            cust_reference=cust_reference,
            trans_date=trans_date,
            val_date=val_date,
            amount=amount,
            cheque_number=cheque_number,
            trans_ref=trans_ref,
            description=description
        )
        transaction.save()

        data = {
                "acc_details":acc_details,
                "cust_reference":cust_reference,
                "trans_date":trans_date,
                "val_date":val_date,
                "amount":amount,
                "trans_ref":trans_ref,
                "description":description,
                "cheque_number":cheque_number
            }
        
        return render(request, 'index.html', context = {'errors': errors,"data":data,"date":date.today()})
    
