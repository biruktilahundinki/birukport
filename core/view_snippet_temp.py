@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # Ensure user is authorized (Customer owner or Admin)
    if not request.user.is_staff and order.customer != request.user:
        return redirect('dashboard')
    
    # Get chat history
    chat_messages = order.messages.all().order_by('timestamp')
    
    return render(request, 'core/order_detail.html', {
        'order': order,
        'chat_messages': chat_messages
    })
