# Meta Package
Name:           ros-iron-moveit
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-iron-moveit and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit
Requires:       ros2-iron-moveit-devel

Obsoletes: ros-iron-moveit < 2.8.0-1

%description
Meta package that contains all essential packages of MoveIt 2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
