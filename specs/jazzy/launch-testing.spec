# Meta Package
Name:           ros-jazzy-launch-testing
Version:        3.4.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-launch_testing and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-launch_testing
Requires:       ros2-jazzy-launch_testing-devel

Obsoletes: ros-jazzy-launch-testing < 3.4.4-1

%description
A package to create tests which involve launch files and multiple
processes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.4-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.2-1
- Update to latest release
