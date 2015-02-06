Summary:	This tool brings Google services to the command line
Name:		googlecl
Version:	0.9.14
Release:	2
License:	ASL 2.0
Group:		Networking/Other
Url:		http://code.google.com/p/googlecl/
Source0:	http://googlecl.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
Requires:	python-gdata
BuildArch:	noarch

%description
GoogleCL is a command-line utility that provides access to various Google
services. It streamlines tasks such as posting to a Blogger blog, adding events
to Calendar, or editing documents on Google Docs.

For example:
$ google blogger post --blog "My blog" --tags "python, googlecl" my_post.html
$ google calendar add "Lunch with Jason tomorrow at noon"
$ google docs edit --title "Shopping list" --editor vim

GoogleCL is a pure Python application that uses the Python gdata libraries to
make Google Data API calls from the command line.

%files
%doc README.txt README.config INSTALL.txt 
%{_mandir}/man1/google.1*
%{_bindir}/google
%{python_sitelib}/%{name}-*.egg-info
%{python_sitelib}/%{name}/*.py*
%{python_sitelib}/%{name}/*/*.py*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --skip-build
mkdir -p %{buildroot}%{_mandir}/man1
cp -a man/google.1 %{buildroot}%{_mandir}/man1

