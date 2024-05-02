# Meta Package
Name:           ros-iron-moveit-ros-benchmarks
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-iron-moveit_ros_benchmarks and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_ros_benchmarks
Requires:       ros2-iron-moveit_ros_benchmarks-devel

Obsoletes: ros-iron-moveit-ros-benchmarks < 2.8.0-1

%description
Enhanced tools for benchmarks in MoveIt

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
