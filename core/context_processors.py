
def context(request):
    return {
        'user_id': request.session['user_id'] if 'user_id' in request.session else None,
        'user_type': request.session['user_type'] if 'user_type' in request.session else None,
    }
