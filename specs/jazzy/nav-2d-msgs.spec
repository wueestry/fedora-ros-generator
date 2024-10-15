# Meta Package
Name:           ros-jazzy-nav-2d-msgs
Version:        1.3.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-nav_2d_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-nav_2d_msgs
Requires:       ros2-jazzy-nav_2d_msgs-devel

Obsoletes: ros-jazzy-nav-2d-msgs < 1.3.2-1

%description
Basic message types for two dimensional navigation, extending from
geometry_msgs::Pose2D.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
