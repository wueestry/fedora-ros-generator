# Meta Package
Name:           ros-jazzy-pcl-msgs
Version:        1.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-pcl_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pcl_msgs
Requires:       ros2-jazzy-pcl_msgs-devel

Obsoletes: ros-jazzy-pcl-msgs < 1.0.0-1

%description
Package containing PCL (Point Cloud Library)-related ROS messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.0-1
- Update to latest release
