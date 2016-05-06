#This package is for EPEL only
# Created by pyp2rpm-3.0.1
%global pypi_name Jinja2

Name:           python-%{pypi_name}
Version:        2.8
Release:        1%{?dist}
Summary:        A small but fast and easy to use stand-alone template engine written in pure python

License:        BSD
URL:            http://jinja.pocoo.org/
Source0:        https://pypi.python.org/packages/f2/2f/0b98b06a345a761bec91a079ccae392d282690c2d8272e708f4d10829e22/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
 
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sphinx

%description

Jinja2
~~~~~~

Jinja2 is a template engine written in pure Python.  It
provides a
`Django`_ inspired non-XML syntax but supports inline expressions
and
an optional `sandboxed`_ environment.

Nutshell
--------

Here a small
example of a Jinja template::

    {% extends 'base.html' %}
    {% block title
%}Memberlist{% endblock %}
    {% block content %}
      <ul>
      {% for user
in users %}
 ...

%package -n     python2-%{pypi_name}
Summary:        A small but fast and easy to use stand-alone template engine written in pure python
 
Requires:       python-MarkupSafe
Requires:       python-setuptools
%description -n python2-%{pypi_name}

Jinja2
~~~~~~

Jinja2 is a template engine written in pure Python.  It
provides a
`Django`_ inspired non-XML syntax but supports inline expressions
and
an optional `sandboxed`_ environment.

Nutshell
--------

Here a small
example of a Jinja template::

    {% extends 'base.html' %}
    {% block title
%}Memberlist{% endblock %}
    {% block content %}
      <ul>
      {% for user
in users %}
 ...

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        A small but fast and easy to use stand-alone template engine written in pure python
 
Requires:       python%{python3_pkgversion}-MarkupSafe
Requires:       python%{python3_pkgversion}-setuptools
%description -n python%{python3_pkgversion}-%{pypi_name}

Jinja2
~~~~~~

Jinja2 is a template engine written in pure Python.  It
provides a
`Django`_ inspired non-XML syntax but supports inline expressions
and
an optional `sandboxed`_ environment.

Nutshell
--------

Here a small
example of a Jinja template::

    {% extends 'base.html' %}
    {% block title
%}Memberlist{% endblock %}
    {% block content %}
      <ul>
      {% for user
in users %}
 ...

%package -n python-%{pypi_name}-doc
Summary:        Jinja2 documentation
%description -n python-%{pypi_name}-doc
Documentation for Jinja2

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build
%{__python3} setup.py build
# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%{__python3} setup.py install --skip-build --root %{buildroot}

%{__python2} setup.py install --skip-build --root %{buildroot}


%files -n python2-%{pypi_name} 
%doc README.rst docs/_themes/LICENSE LICENSE
%{python2_sitelib}/jinja2
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python%{python3_pkgversion}-%{pypi_name} 
%doc README.rst docs/_themes/LICENSE LICENSE
%{python3_sitelib}/jinja2
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Fri May 06 2016 Michal Cyprian <mcyprian@redhat.com> - 2.8-1
- Initial package.
