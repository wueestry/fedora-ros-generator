# Meta Package
Name:           ros-iron-rqt-image-view
Version:        1.2.0
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_image_view
Summary:        Meta package for ros2-iron-rqt_image_view and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_image_view
Requires:       ros2-iron-rqt_image_view-devel

Obsoletes: ros-iron-rqt-image-view < 1.2.0-1

%description
rqt_image_view provides a GUI plugin for displaying images using
image_transport.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.0-1
- Update to latest release
