Summary:	Utility to convert from Mandriva ldetect to LTSP format
Name:		ldetect2ltsp
Version:	1.0
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://www.ltsp.org
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


