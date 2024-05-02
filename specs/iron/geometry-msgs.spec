# Meta Package
Name:           ros-iron-geometry-msgs
Version:        5.0.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-geometry_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-geometry_msgs
Requires:       ros2-iron-geometry_msgs-devel

Obsoletes: ros-iron-geometry-msgs < 5.0.0-1

%description
A package containing some geometry related message definitions.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.5.0.0-1
- Update to latest release
