%define	name	svnauthcheck
%define	version	1.0.3
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Tool to check the syntax of subversion acl file
License:    GPLv2+
Group:      Development/Other 
URL:        https://svn.id.ethz.ch/docs/svnauthcheck.html
Source:     https://svn.id.ethz.ch/files/%{name}-%{version}.tar.bz2
Patch:      svnauthcheck-1.0.2-fix-format-errors.patch
BuildRequires:  flex
BuildRequires:  bison
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
svnauthcheck is a tool to check the syntax of Subversion access control files.
It was developed to be able to delegate to certain repository users the ability
to manage the access control to the repository itself.

%prep
%setup -q
%patch -p 1

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

