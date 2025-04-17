# Meta Package
Name:           ros-jazzy-gz-fuel-tools-vendor
Version:        0.0.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-fuel-tools
Summary:        Meta package for ros2-jazzy-gz_fuel_tools_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_fuel_tools_vendor
Requires:       ros2-jazzy-gz_fuel_tools_vendor-devel

Obsoletes: ros-jazzy-gz-fuel-tools-vendor < 0.0.6-1

%description
Vendor package for: gz-fuel_tools9 9.1.1 Gazebo Fuel Tools: Classes
and tools for interacting with Gazebo Fuel

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.6-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.5-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.3-1
- Update to latest release
