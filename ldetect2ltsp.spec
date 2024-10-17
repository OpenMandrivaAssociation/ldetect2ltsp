Summary:	Utility to convert from Mandriva ldetect to LTSP format
Name:		ldetect2ltsp
Version:	1.0
Release:	6
License:	GPL
Group:		System/Servers
URL:		https://www.ltsp.org
Source0:	ldetect2ltsp
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This program will read in a device database of PCI Vendor/Device Ids and a
Video card database in the Mandriva ldetect-lst format, and will convert
them into the LTSP format, for use with pci_scan.

%prep

%setup -q -c -T

cp %{SOURCE0} %{name}

%install
rm -rf %{buildroot}

install -d  %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2011.0
+ Revision: 620062
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 429709
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 248336
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-1mdv2008.1
+ Revision: 136535
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2007.0
+ Revision: 117093
- Import ldetect2ltsp

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdk
- initial Mandriva package (mille-xterm import)

