# Meta Package
Name:           ros-jazzy-test-msgs
Version:        2.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-test_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-test_msgs
Requires:       ros2-jazzy-test_msgs-devel

Obsoletes: ros-jazzy-test-msgs < 2.0.2-1

%description
A package containing message definitions and fixtures used exclusively
for testing purposes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.2-1
- Update to latest release
