# Meta Package
Name:           ros-iron-rviz-common
Version:        12.4.7
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/ros2/rviz/blob/ros2/README.md
Summary:        Meta package for ros2-iron-rviz_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rviz_common
Requires:       ros2-iron-rviz_common-devel

Obsoletes: ros-iron-rviz-common < 12.4.7-1

%description
Common rviz API, used by rviz plugins and applications.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.12.4.7-1
- Update to latest release
