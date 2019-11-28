from django.shortcuts import render
from github import Github
from .models import Commit
from .. import secret
from ..repositories.models import Repository


def get_commits(request):
    """
    Falta se livrar dessa parte aqui e só pegar o id que o usuário escolher
    """

    g = Github(secret.login, secret.password)
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil")
    commits = repo.get_commits()
    total_commits = commits.totalCount
    # for commit in repo.get_commits():
    #     commit_model = Commit.objects.create(shaCommit=commit.sha, author=commit.commit.author.name, date=commit.commit.author.date)
    #     commit_model.publish()

    # print(commit.commit.author.date)
    if bool(Commit.objects.filter(repository__repositoryID=repo.id)):
        commits = Commit.objects.filter(repository__repositoryID=repo.id)
        author1 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'Matheus-AM')
        author1 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'Matheus-AM')
        author2 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'KalebeLopes')
        author3 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'joao15victor08')
        author4 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'ailamaralves')
        author5 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'muriloschiler')
        author6 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'damarcones')

        date1o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=1)
        date2o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=2)
        date3o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=3)
        date4o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=4)
        date5o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=5)
        date6o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=6)
        date7o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=7)
        date8o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=8)
        date9o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=9)
        date10o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=10)
        date11o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=11)
        date12o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=12)

        date1c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=1 )
        date2c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=2 )
        date3c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=3)
        date4c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=4)
        date5c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=5)
        date6c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=6)
        date7c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=7)
        date8c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=8)
        date9c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=9)
        date10c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=10)
        date11c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=11)
        date12c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=12)

    else:
        raise TypeError

    return render(request, 'commits.html', {'commits': commits,'total_commits': total_commits,'author1': author1,'author2': author2,'author3': author3,'author4': author4,'author5': author5,'author6': author6,
     'date1o': date1o, 'date2o': date2o,'date3o': date3o,'date4o': date4o,'date5o': date5o,'date6o': date6o,
    'date7o': date7o,'date8o': date8o,'date9o': date9o,'date10o': date10o,'date11o': date11o,'date12o': date12o, 'date1c': date1c, 'date2c': date2c,
    'date3c': date3c,'date4c': date4c,'date5c': date5c,'date6c': date6c, 'date7c': date7c,'date8c': date8c,'date9c': date9c,'date10c': date10c,
    'date11c': date11c,'date12c': date12c})






def refresh_commit(repository):
    Commit.objects.all().exclude(repository=repository)
    g = Github(login_or_token=secret.login, password=secret.password)
    repo = g.get_repo(full_name_or_id=repository.repositoryID)
    for commit in repo.get_commits():
        commit_model = Commit.objects.create(repository=repository,
                                             sha_commit=commit.sha,
                                             author=commit.commit.author.name,
                                             date=commit.commit.author.date)
        commit_model.publish()
