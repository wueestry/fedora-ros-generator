# Meta Package
Name:           ros-iron-gazebo-dev
Version:        3.7.0
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://gazebosim.org/tutorials?cat=connect_ros
Summary:        Meta package for ros2-iron-gazebo_dev and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-gazebo_dev
Requires:       ros2-iron-gazebo_dev-devel

Obsoletes: ros-iron-gazebo-dev < 3.7.0-1

%description
Provides a cmake config for the default version of Gazebo for the ROS
distribution.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.7.0-1
- Update to latest release
