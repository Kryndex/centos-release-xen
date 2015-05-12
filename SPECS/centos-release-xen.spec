Summary: CentOS6 Xen Support repo configs
Name: centos-release-xen
Epoch: 10
Version: 6
Release: 4.el6.centos
License: GPL
Group: System Environment/Base
Source: centos-release-xen-%{version}-%{release}.tar.gz
Source1: xen-kernel
URL: http://wiki.centos.org/QaWiki/Xen4

Provides: centos-release-xen
Requires: centos-release = 6

BuildRoot: %{_tmppath}/centos-release-xen-root

%description
yum Configs and some docs on the Xen-4 stack included in CentOS-6 

%prep
%setup -q  -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p -m 755 $RPM_BUILD_ROOT/%{_bindir}
for file in CentOS*repo ; do
  install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
done
install -m 744 grub-bootxen.sh $RPM_BUILD_ROOT/%{_bindir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/xen-kernel
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) /etc/yum.repos.d/*
%{_bindir}/grub-bootxen.sh
%config(noreplace) /etc/sysconfig/xen-kernel


%changelog
* Mon Oct 20 2014 Johnny Hughes <johnny@centos.org> - 6-4.el6.centos
- shifted /etc/sysconfig/xen-kernel to centos-xen-release

* Thu Oct  9 2014 Johnny Hughes <johnny@centos.org> - 6-3.el6.centos
- Modified grub-bootxen.sh to allow for automatic grub updates for kernel install

* Wed Jun 19 2013 Karanbir Singh <kbsingh@centos.org> - 6-2.el6.centos
- Update to release

* Thu Jan 31 2013 Karanbir Singh <kbsingh@centos.org> - 6-0.el6.centos
- Build for CentOS Xen Beta release
