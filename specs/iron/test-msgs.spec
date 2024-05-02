# Meta Package
Name:           ros-iron-test-msgs
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-test_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-test_msgs
Requires:       ros2-iron-test_msgs-devel

Obsoletes: ros-iron-test-msgs < 1.6.0-1

%description
A package containing message definitions and fixtures used exclusively
for testing purposes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.0-1
- Update to latest release
