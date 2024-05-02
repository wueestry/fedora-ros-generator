# Meta Package
Name:           ros-iron-nav2-amcl
Version:        1.2.7
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav2_amcl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav2_amcl
Requires:       ros2-iron-nav2_amcl-devel

Obsoletes: ros-iron-nav2-amcl < 1.2.7-1

%description
ROS iron package nav2_amcl.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
