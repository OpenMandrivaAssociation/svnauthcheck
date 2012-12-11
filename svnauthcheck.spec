%define	name	svnauthcheck
%define	version	1.0.12
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Tool to check the syntax of subversion acl file
License:    GPLv2+
Group:      Development/Other 
URL:        https://svn.id.ethz.ch/docs/svnauthcheck.html
Source:     https://svn.id.ethz.ch/files/%{name}-%{version}.tar.bz2
BuildRequires:  flex
BuildRequires:  bison
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
svnauthcheck is a tool to check the syntax of Subversion access control files.
It was developed to be able to delegate to certain repository users the ability
to manage the access control to the repository itself.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Fri May 20 2011 Funda Wang <fwang@mandriva.org> 1.0.12-1mdv2011.0
+ Revision: 676227
- new version 1.0.12

* Tue Dec 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.11-1mdv2011.0
+ Revision: 625515
- update to new version 1.0.11

* Sun Sep 05 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.9-1mdv2011.0
+ Revision: 576176
- update to new version 1.0.9

* Fri Jul 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.8-1mdv2011.0
+ Revision: 554131
- update to new version 1.0.8

* Wed Jan 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-1mdv2010.1
+ Revision: 494368
- new version

* Thu Aug 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-1mdv2010.0
+ Revision: 418408
- update to new version 1.0.3

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 384535
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.10.6-3mdv2009.0
+ Revision: 269397
- rebuild early 2009.0 package (before pixel changes)

* Mon May 26 2008 Michael Scherer <misc@mandriva.org> 0.10.6-2mdv2009.0
+ Revision: 211356
- correct the license, the group and the summary

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10.6-1mdv2009.0
+ Revision: 210861
- new version

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10.5-1mdv2008.1
+ Revision: 159898
- import svnauthcheck


* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.2-1mdv2008.1
- first mdv release  
