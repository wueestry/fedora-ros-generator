# Meta Package
Name:           ros-jazzy-gz-plugin-vendor
Version:        0.0.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-plugin
Summary:        Meta package for ros2-jazzy-gz_plugin_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_plugin_vendor
Requires:       ros2-jazzy-gz_plugin_vendor-devel

Obsoletes: ros-jazzy-gz-plugin-vendor < 0.0.4-1

%description
Vendor package for: gz-plugin2 2.0.3 Gazebo Plugin : Cross-platform
C++ library for dynamically loading plugins.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
