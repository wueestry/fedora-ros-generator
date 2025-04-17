# Meta Package
Name:           ros-jazzy-gz-gui-vendor
Version:        0.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-rendering
Summary:        Meta package for ros2-jazzy-gz_gui_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_gui_vendor
Requires:       ros2-jazzy-gz_gui_vendor-devel

Obsoletes: ros-jazzy-gz-gui-vendor < 0.0.5-1

%description
Vendor package for: gz-gui8 8.4.0 Gazebo GUI : Graphical interfaces
for robotics applications

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.5-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.3-1
- Update to latest release
