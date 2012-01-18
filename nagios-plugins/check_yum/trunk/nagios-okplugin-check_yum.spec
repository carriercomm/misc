%define debug_package %{nil}

Summary:	Nagios plugin to test for Yum updates on RedHat/CentOS Linux.
Name:		nagios-okplugin-check_yum
Version:	0.7.2
Release:	2%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		http://opensource.is/trac/wiki/check_yum
Source0:	http://opensource.ok.is/trac/browser/nagios-plugins/check_yum/releases/nagios-okplugin-check_yum-%{version}.tar.gz
Requires:	yum-security
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager:	Pall Sigurdsson <palli@opensource.is>
BuildArch: noarch


%description
Nagios plugin to test for Yum updates on RedHat/CentOS Linux.

%prep
%setup -q
perl -pi -e "s|/usr/lib/|%{_libdir}/|g" nrpe.d/check_yum.cfg
perl -pi -e "s|/usr/lib64/|%{_libdir}/|g" nrpe.d/check_yum.cfg

%build


%install
rm -rf %{buildroot}
install -D -p -m 0755 check_yum %{buildroot}%{_libdir}/nagios/plugins/check_yum
install -D -p -m 0755 nrpe.d/check_yum.cfg %{buildroot}/etc/nrpe.d/check_yum.cfg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/nagios/plugins/*
/etc/nrpe.d/check_yum.cfg

%changelog
* Mon Sep 14 2010  Pall Sigurdsson <palli@opensource.is> 0.1-1
- Initial packaging
