Name:    googlecl
Version: 0.9.11
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


%changelog
* Tue Nov 23 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.9.11-1mdv2011.0
+ Revision: 600268
- Updated to 0.9.11.

* Fri Nov 12 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0.9.10-2mdv2011.0
+ Revision: 596947
- rebuild for python 2.7

* Thu Sep 23 2010 Funda Wang <fwang@mandriva.org> 0.9.10-1mdv2011.0
+ Revision: 580755
- update to new version 0.9.10

* Sun Jun 20 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.9.5-1mdv2010.1
+ Revision: 548345
- Added manpage and deps
- Imported googlecl.
- Created package structure for googlecl.

