# Meta Package
Name:           ros-jazzy-ros2-control-test-assets
Version:        4.11.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2_control_test_assets and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2_control_test_assets
Requires:       ros2-jazzy-ros2_control_test_assets-devel

Obsoletes: ros-jazzy-ros2-control-test-assets < 4.11.0-1

%description
The package provides shared test resources for ros2_control stack

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.11.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.8.0-1
- Update to latest release
