# Django - Multi-Language

Funcionalidade para customizar os idiomas utilizados na aplicação.

> Aprendizados:
Componentes-Hooks-Contexto de Autenticação-Autenticação com Google-Base de dados no Firebase-Typescript

### Procedimentos

> Instalação de compilador em Windows

* Documentação: [https://docs.djangoproject.com/en/3.2/topics/i18n/translation/](https://docs.djangoproject.com/en/3.2/topics/i18n/translation)

> Após criado pastas de idiomas em _locale_

- locale
    - en
    - fr

> Execute o comando `python manage.py makemessages --all` para criar os arquivos _django.po_ para trazer as palavras e frases estáticas da aplicação nos idiomas configurados
> Traduza as frases e palavras nos arquivos _django.po_
> Execute o comando `python manage.py compilemessages` para compilar as traduções
