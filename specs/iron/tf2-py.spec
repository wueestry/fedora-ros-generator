# Meta Package
Name:           ros-iron-tf2-py
Version:        0.31.6
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/tf2_py
Summary:        Meta package for ros2-iron-tf2_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tf2_py
Requires:       ros2-iron-tf2_py-devel

Obsoletes: ros-iron-tf2-py < 0.31.6-1

%description
The tf2_py package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.6-1
- Update to latest release
