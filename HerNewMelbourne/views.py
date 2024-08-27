from django.shortcuts import render

def landingPage(request):
    return render(request, 'LandingPage.html')

def homePage(request):
    return render(request, 'HomePage.html')

def scenarioRolePlay(request):
    return render(request, 'ScenarioRolePlay.html')

def scenarioRolePlayList(request):
    return render(request, 'ScenarioRolePlayList.html')


