# Meta Package
Name:           ros-jazzy-ros2lifecycle-test-fixtures
Version:        0.32.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2lifecycle_test_fixtures and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2lifecycle_test_fixtures
Requires:       ros2-jazzy-ros2lifecycle_test_fixtures-devel

Obsoletes: ros-jazzy-ros2lifecycle-test-fixtures < 0.32.1-1

%description
Package containing fixture nodes for ros2lifecycle tests

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.32.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.32.0-1
- Update to latest release
