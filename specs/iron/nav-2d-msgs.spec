# Meta Package
Name:           ros-iron-nav-2d-msgs
Version:        1.2.7
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav_2d_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav_2d_msgs
Requires:       ros2-iron-nav_2d_msgs-devel

Obsoletes: ros-iron-nav-2d-msgs < 1.2.7-1

%description
Basic message types for two dimensional navigation, extending from
geometry_msgs::Pose2D.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
