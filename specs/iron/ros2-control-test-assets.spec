# Meta Package
Name:           ros-iron-ros2-control-test-assets
Version:        3.24.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ros2_control_test_assets and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ros2_control_test_assets
Requires:       ros2-iron-ros2_control_test_assets-devel

Obsoletes: ros-iron-ros2-control-test-assets < 3.24.0-1

%description
The package provides shared test resources for ros2_control stack

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
