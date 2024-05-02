# Meta Package
Name:           ros-iron-launch-testing
Version:        2.0.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-launch_testing and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-launch_testing
Requires:       ros2-iron-launch_testing-devel

Obsoletes: ros-iron-launch-testing < 2.0.3-1

%description
A package to create tests which involve launch files and multiple
processes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.3-1
- Update to latest release
