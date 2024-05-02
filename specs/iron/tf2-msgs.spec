# Meta Package
Name:           ros-iron-tf2-msgs
Version:        0.31.6
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/tf2_msgs
Summary:        Meta package for ros2-iron-tf2_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tf2_msgs
Requires:       ros2-iron-tf2_msgs-devel

Obsoletes: ros-iron-tf2-msgs < 0.31.6-1

%description
tf2_msgs

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.6-1
- Update to latest release
