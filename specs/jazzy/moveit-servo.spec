# Meta Package
Name:           ros-jazzy-moveit-servo
Version:        2.12.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://moveit.github.io/moveit_tutorials
Summary:        Meta package for ros2-jazzy-moveit_servo and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_servo
Requires:       ros2-jazzy-moveit_servo-devel

Obsoletes: ros-jazzy-moveit-servo < 2.12.2-1

%description
Provides real-time manipulator Cartesian and joint servoing.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.12.2-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.12.1-1
- Update to latest release
* Thu Nov 21 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-2
- Rebuild due to srdfdom update
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
