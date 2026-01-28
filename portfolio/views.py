from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Profile, Skill, Project, Experience, Service, ContactMessage, Testimonial, PortfolioDocument


def portfolio_home(request):
    """Main portfolio page"""
    context = {
        'profile': Profile.objects.first(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'featured_projects': Project.objects.filter(featured=True)[:3],
        'experiences': Experience.objects.all(),
        'services': Service.objects.all(),
        'testimonials': Testimonial.objects.filter(is_active=True),
        'documents': PortfolioDocument.objects.all(),
    }
    return render(request, 'portfolio/index.html', context)


def project_detail(request, slug):
    """Individual project detail page"""
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'related_projects': related_projects
    })


def contact_submit(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        try:
            ContactMessage.objects.create(
                name=request.POST.get('name', ''),
                email=request.POST.get('email', ''),
                subject=request.POST.get('subject', ''),
                message=request.POST.get('message', ''),
                project_type=request.POST.get('project_type', ''),
                budget=request.POST.get('budget', ''),
            )
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Thank you! Your message has been sent.'})
            
            messages.success(request, 'Thank you! Your message has been sent. I will get back to you soon.')
            return redirect('portfolio:home')
        
        except Exception as e:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Something went wrong. Please try again.'})
            
            messages.error(request, 'Something went wrong. Please try again.')
            return redirect('portfolio:home')
    
    return redirect('portfolio:home')


def projects_api(request):
    """API endpoint for project filtering"""
    category = request.GET.get('category', 'all')
    
    if category == 'all':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category=category)
    
    data = [{
        'id': p.id,
        'title': p.title,
        'slug': p.slug,
        'short_description': p.short_description,
        'image_url': p.image_url.url if p.image_url else '',
        'category': p.category,
        'technologies': p.get_tech_list(),
        'github_url': p.github_url,
        'live_url': p.live_url,
        'featured': p.featured,
    } for p in projects]
    
    return JsonResponse({'projects': data})
