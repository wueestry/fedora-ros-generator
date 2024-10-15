# Meta Package
Name:           ros-jazzy-gz-tools-vendor
Version:        0.0.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-tools
Summary:        Meta package for ros2-jazzy-gz_tools_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_tools_vendor
Requires:       ros2-jazzy-gz_tools_vendor-devel

Obsoletes: ros-jazzy-gz-tools-vendor < 0.0.4-1

%description
Vendor package for: gz-tools2 2.0.1 Gazebo Tools: Entrypoint to
Gazebo's command line interface

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
