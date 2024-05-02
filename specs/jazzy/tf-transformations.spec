# Meta Package
Name:           ros-jazzy-tf-transformations
Version:        1.0.1
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tf_transformations and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tf_transformations
Requires:       ros2-jazzy-tf_transformations-devel

Obsoletes: ros-jazzy-tf-transformations < 1.0.1-1

%description
Reimplementation of the tf/transformations.py library for common
Python spatial operations

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.1-1
- Update to latest release
