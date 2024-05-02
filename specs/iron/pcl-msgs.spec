# Meta Package
Name:           ros-iron-pcl-msgs
Version:        1.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-pcl_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-pcl_msgs
Requires:       ros2-iron-pcl_msgs-devel

Obsoletes: ros-iron-pcl-msgs < 1.0.0-1

%description
Package containing PCL (Point Cloud Library)-related ROS messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.0-1
- Update to latest release
