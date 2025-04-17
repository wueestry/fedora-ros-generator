# Meta Package
Name:           ros-jazzy-sdformat-vendor
Version:        0.0.9
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/sdformat
Summary:        Meta package for ros2-jazzy-sdformat_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-sdformat_vendor
Requires:       ros2-jazzy-sdformat_vendor-devel

Obsoletes: ros-jazzy-sdformat-vendor < 0.0.9-1

%description
Vendor package for: sdformat14 14.7.0 SDFormat is an XML file format
that describes environments, objects, and robots in a manner suitable
for robotic applications

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.9-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.8-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.7-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.6-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.5-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
