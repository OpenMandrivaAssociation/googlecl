Name:    googlecl
Version: 0.9.5
Release: %mkrel 1
Summary: GoogleCL brings Google services to the command line
License: Apache License 2.0
URL:     http://code.google.com/p/googlecl/
Group:   Networking/Other
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source: http://googlecl.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires: python python-devel
Requires: python
Requires: python-gdata

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

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
PYTHONDONTWRITEBYTECODE= python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mkdir -p %{buildroot}%{_mandir}/man1
install -m0644 man/google.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.txt README.config INSTALL.txt 
%{_mandir}/man1/google.1*
